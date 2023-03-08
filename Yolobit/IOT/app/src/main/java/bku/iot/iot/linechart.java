package bku.iot.iot;
import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Color;
import android.os.Bundle;
import android.util.Log;
import android.widget.AbsListView;
import android.widget.LinearLayout;
import android.widget.RelativeLayout;
import android.widget.TextView;

import com.github.angads25.toggle.interfaces.OnToggledListener;
import com.github.angads25.toggle.model.ToggleableView;
import com.github.angads25.toggle.widget.LabeledSwitch;

import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallbackExtended;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;

import java.nio.charset.Charset;

import com.github.mikephil.charting.components.Legend;
import com.github.mikephil.charting.components.XAxis;
import com.github.mikephil.charting.components.YAxis;
import com.github.mikephil.charting.data.LineData;
import com.github.mikephil.charting.data.LineDataSet;
import com.github.mikephil.charting.data.Entry;
import com.github.mikephil.charting.charts.LineChart;
import com.github.mikephil.charting.interfaces.datasets.ILineDataSet;
import com.github.mikephil.charting.utils.ColorTemplate;

import java.util.ArrayList;

import bku.iot.iot.R;

public class linechart extends AppCompatActivity {

    private RelativeLayout mainLayout;
    private LineChart mChart;
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.chart);
        //mainLayout = (RelativeLayout) findViewById(R.id.lineChart) ;
        //    mChart = findViewById(R.id.lineChart);
        LineChart chart = findViewById(R.id.lineChart);
        ArrayList Temp = new ArrayList();

        Temp.add(new Entry(0, 20f));
        Temp.add(new Entry(1, 10f));
        Temp.add(new Entry(2, 29f));
        Temp.add(new Entry(3, 30f));
        Temp.add(new Entry(4, 55f));
        Temp.add(new Entry(5, 57f));


        LineDataSet ldataset = new LineDataSet(Temp, "Temperature");
        chart.animateY(5000);
        LineData data = new LineData(ldataset);
        ldataset.setColors(Color.rgb(255,0,0));
        chart.setData(data);

        mChart = new LineChart(this);

        //      mainLayout.addView(mChart);
//        mainLayout.addView(mChart, new AbsListView.LayoutParams(AbsListView.LayoutParams.MATCH_PARENT, AbsListView.LayoutParams.MATCH_PARENT));

        mChart.setNoDataText("No data");

//        mChart.setDefaultFocusHighlightEnabled(true);

        mChart.setTouchEnabled(true);

        mChart.setDragEnabled(true);
        mChart.setSaveEnabled(true);
        mChart.setDrawGridBackground(false);

        mChart.setPinchZoom(true);

        mChart.setBackgroundColor(Color.LTGRAY);

        //      LineData data = new LineData();
        data.setValueTextColor(Color.WHITE);

        mChart.setData(data);

        Legend l = mChart.getLegend();

        l.setForm(Legend.LegendForm.LINE);
        l.setTextColor(Color.WHITE);

        XAxis x1 = mChart.getXAxis();
        x1.setTextColor(Color.WHITE);
        x1.setDrawGridLines(false);
        x1.setAvoidFirstLastClipping(true);

        YAxis y1 = mChart.getAxisLeft();
        y1.setTextColor(Color.WHITE);
        y1.setAxisMaxValue(140f);
        y1.setDrawGridLines(true);

        YAxis y12 = mChart.getAxisRight();
        y12.setEnabled(false);
    }

    @Override
    protected void onResume(){
        super.onResume();

        new Thread(new Runnable(){
            @Override
            public void run(){
                for(int i = 0; i < 100; i++){
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            addEntry();
                        }
                    });
                    try{
                        Thread.sleep(600);
                    } catch (InterruptedException e){

                    }
                }
            }
        }).start();
    }

    private void addEntry(){
        LineData data = mChart.getData();

        if(data != null){
            LineDataSet set = (LineDataSet) data.getDataSetByIndex(0);

//            if(set == null){
//                set = createSet();
//                data.addDataSet(set);
//            }


            data.addEntry(new Entry((float) (Math.random() * 120) + 6f, set.getEntryCount()), 0);

            mChart.notifyDataSetChanged();

            mChart.setVisibleXRange(1, 6);

            mChart.moveViewToX(data.getEntryCount());
        }
    }
//
//    private LineDataSet createSet(){
//        LineDataSet set = new LineDataSet(null, "SPL");
//        set.setAxisDependency(YAxis.AxisDependency.LEFT);
//        set.setColor(ColorTemplate.getHoloBlue());
//        set.setCircleColor(ColorTemplate.getHoloBlue());
//        set.setLineWidth(2f);
//        set.setFillAlpha(65);
//        set.setFillColor(ColorTemplate.getHoloBlue());
//        set.setHighLightColor(Color.rgb(244, 117, 177));
//        set.setValueTextSize(10f);
//        set.setValueTextColor(Color.WHITE);
//
//        return set;
//    }

}
