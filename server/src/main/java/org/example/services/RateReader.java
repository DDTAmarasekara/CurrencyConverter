package org.example.services;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class RateReader {


    Map<String,Double> rates = new HashMap<>();


    public  Map<String,Double> JsonFileRead(String filePath) {
        JSONParser jsonParser = new JSONParser();

        try {
            FileReader fileRead = new FileReader(filePath);

            Object object = jsonParser.parse(fileRead);
            JSONObject jsonObject = (JSONObject) object;

            JSONObject jsonObject1 = (JSONObject) jsonObject.get("rates");

            jsonObject1.forEach((key, value) -> rates.put((String) key, Double.parseDouble(value.toString())));




        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ParseException e) {
            e.printStackTrace();
        }
        return rates;
    }
}
