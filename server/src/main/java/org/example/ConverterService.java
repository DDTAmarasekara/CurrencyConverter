package org.example;

import org.example.services.RateReader;

import javax.jws.WebMethod;
import javax.jws.WebService;
import java.util.Map;

@WebService
public class ConverterService {

    private Map<String,Double> rates;
    RateReader fileReader;


    public ConverterService() {
        fileReader = new RateReader();
        String filepath = "src/main/java/org/example/services/currency.json";
        this.rates = fileReader.JsonFileRead(filepath);
    }

    @WebMethod
    public double converter(String source, double amount, String target){
        double dollerAmount = convertToDollar(source,amount);

        return dollarToFinalCurrency(dollerAmount,rates.get(target));
    }


    public double convertToDollar(String source, double amount) {
        double baseCurrency = rates.get(source);
        double ctd = amount/baseCurrency;
        return ctd;
    }

    public double dollarToFinalCurrency(double amount, double rate) {
        return rate*amount;

    }



}

