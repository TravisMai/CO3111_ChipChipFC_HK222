package bku.iot.iot;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.github.angads25.toggle.interfaces.OnToggledListener;
import com.github.angads25.toggle.model.ToggleableView;
import com.github.angads25.toggle.widget.LabeledSwitch;

import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallbackExtended;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;

import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.Timer;
import java.util.TimerTask;
class signal {
    public static String sign = "0";
    public static int counter = 0;
    public static String error_count = "0";
    public static boolean adaConnect = false;
}
public class MainActivity extends AppCompatActivity {
    MQTTHelper mqttHelper;
    Button txtTemp;
    TextView  txtH, txtL, txtA, txtS, txtC;
    LabeledSwitch btn1, btn2;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        txtTemp = findViewById(R.id.txtTemp);
        txtH = findViewById(R.id.txtHumi);
        txtL = findViewById(R.id.txtLight);
        txtA = findViewById(R.id.txtAI);
        txtS = findViewById(R.id.txtSM);
        btn1 = findViewById(R.id.btn1);
        btn2 = findViewById(R.id.btn2);
        btn1.setEnabled(false);
        btn2.setEnabled(false);
        txtC = findViewById(R.id.txtCnt);
        btn1.setOnToggledListener(new OnToggledListener() {
            @Override
            public void onSwitched(ToggleableView toggleableView, boolean isOn) {
                if(isOn == true){
                    sendDataMQTT("EmChes/feeds/nutnhan1","1");
                }else{
                    sendDataMQTT("EmChes/feeds/nutnhan1","0");
                }
            }
        });
        btn2.setOnToggledListener(new OnToggledListener() {
            @Override
            public void onSwitched(ToggleableView toggleableView, boolean isOn) {
                if(isOn == true){
                    sendDataMQTT("EmChes/feeds/nutnhan2","3");
                }else{
                    sendDataMQTT("EmChes/feeds/nutnhan2","2");
                }
            }
        });
        txtTemp.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent I = new Intent(MainActivity.this, linechart.class);
                startActivity(I);
            }
        });
        startMQTT();
    }
    public void sendDataMQTT(String topic, String value)
    {
        MqttMessage msg = new MqttMessage();
        msg.setId(1234);
        msg.setQos(0);
        msg.setRetained(false);

        byte[] b = value.getBytes(Charset.forName("UTF-8"));
        msg.setPayload(b);

        try {
            mqttHelper.mqttAndroidClient.publish(topic, msg);
        } catch (MqttException e){
        }
    }
    private  void timer_isr(){
        Timer aTimer = new Timer();
        TimerTask aTask = new TimerTask() {
            @Override
            public void run() {
                // TODO
                if((signal.counter < 3)&&(signal.adaConnect)){
                    signal.counter = signal.counter + 1;
                    signal.sign = "0";
                    sendDataMQTT("EmChes/feeds/signal","0");
                }
//                else{
//                    if((!signal.adaConnect)&&(signal.counter<3)){
//                        signal.error_count = signal.error_count + 1;
//                    }
//                }
            }
        };
        aTimer.schedule(aTask, 10000, 15000);
    }
    public void startMQTT(){
        mqttHelper = new MQTTHelper(this);
        mqttHelper.setCallback(new MqttCallbackExtended() {
            @Override
            public void connectComplete(boolean reconnect, String serverURI) {
                if(signal.error_count.equals("1")){
                    mqttHelper.connect();
                }
                signal.adaConnect = true;
                signal.sign = "0";
                sendDataMQTT("EmChes/feeds/signal","0");
            }

            @Override
            public void connectionLost(Throwable cause) {
                signal.error_count = "1";
                signal.adaConnect = false;
                txtC.setText("Lost");
                btn1.setEnabled(false);
                btn2.setEnabled(false);
            }

            @Override
            public void messageArrived(String topic, MqttMessage message) throws Exception {
                Log.d("TEST", topic + "***" + message.toString());
                if(/* Đúng gói tin đang chờ đợi */true){
                    ack_received = 1;
                }
                if(topic.contains("signal") && message.toString().equals("1")) {
                    signal.sign = "1";
                    signal.counter = 0;
                }
                if(signal.sign.equals("1") && signal.adaConnect){
                    txtC.setText("Connected");
                    btn1.setEnabled(true);
                    btn2.setEnabled(true);
                }else{
                    txtC.setText("Disconnected");
                    btn1.setEnabled(false);
                    btn2.setEnabled(false);
                }
                if(topic.contains("cambien1")){
                    txtTemp.setText(message.toString()+"\n"+"°C");
                }else if(topic.contains("cambien2")){
                    txtH.setText(message.toString()+"\n"+"%");
                }else if(topic.contains("cambien3")){
                    txtL.setText(message.toString()+"\n"+"LUX");
                }else if(topic.contains("ai")){
                    txtA.setText(message.toString());
                }else if(topic.contains("nutnhan1")){
                    if(message.toString().equals("1")){
                        btn1.setOn(true);
                    }
                    else{
                        btn1.setOn(false);
                    }
                }else if(topic.contains("nutnhan2")){
                    if(message.toString().equals("3")){
                        btn2.setOn(true);
                    }
                    else{
                        btn2.setOn(false);
                    }
                }
            }

            @Override
            public void deliveryComplete(IMqttDeliveryToken token) {

            }
        });
        timer_isr();
    }

    ArrayList<String> buffer = new ArrayList<>();
    int counter = 0;
    int ack_received = 0;
    int failures = 0;
    int status = 0;
    public void stop_and_wait(){
        switch (status){
            case 0:
                if (buffer.size()>0){
                    status = 1;
                    failures = 0;
                }
                break;
            case 1:
                String data = buffer.get(0);
                sendDataMQTT("yourtopic", data);
                counter = 3; //3 seconds
                status = 2;
                ack_received = 0;
                break;
            case 2:
                counter --;
                if (counter == 0){
                    status = 1;
                    failures ++;
                }
                if(ack_received == 1){
                    status = 0;
                    buffer.remove(0);
                }
                if (failures >= 3){
                    status = 3;
                }
                break;
            case 3:
                break;
        }
    }
}
