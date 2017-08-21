
public class Wasserkostenabrechnung
{
    private double wasserPrevWarm; 
    private double wasserNewWarm;
    private double wasserPrevKalt; 
    private double wasserNewKalt;
    private double mwStWasser = 0.07;
    private double arbeitspreis;
    private double verrechnungspreis;
    private double tage;
    private double schmutzwasserPreis;
    String newline = System.getProperty("line.separator");
    public Wasserkostenabrechnung(double wasserPrevWarm, double wasserNewWarm, double wasserPrevKalt, 
                                    double wasserNewKalt, double arbeitspreis, double verrechnungspreis, 
                                    double tage, double schmutzwasserPreis)
    {
        this.wasserPrevWarm = wasserPrevWarm;
        this.wasserNewWarm = wasserNewWarm;
        this.wasserPrevKalt = wasserPrevKalt;
        this.wasserNewKalt = wasserNewKalt;
        this.arbeitspreis = arbeitspreis;
        this.verrechnungspreis = verrechnungspreis;
        this.tage = tage;
        this.schmutzwasserPreis = schmutzwasserPreis;
    }
    
    public double wohnFaktor(){
        double result = this.tage / 365.0;
        System.out.println("Faktor: " + this.tage + "/365 Tage");
        return result;
    }
    
    public double schmutzwasserKosten(){
        double result;
        result = wasserverbrauch() * this.schmutzwasserPreis;
        System.out.println(result);
        return result;
    }
    
    public double wasserverbrauch(){
        double wasserverbrauch;
        wasserverbrauch = (this.wasserNewWarm - this.wasserPrevWarm) + (this.wasserNewKalt - this.wasserPrevKalt);
        return wasserverbrauch;
    }
    
    public double wasserKostenBerechnung(){
        double result = wasserverbrauch() * this.arbeitspreis + wohnFaktor() * this.verrechnungspreis;
        result = result * (1 + this.mwStWasser);
        System.out.println(result);
        System.out.println("Wasserverbrauch: " + newline + "Warm-Wasser: " + wasserNewWarm + " - " + wasserPrevWarm + " = ");
        result = result * schmutzwasserKosten();
        return result;
    }
}
