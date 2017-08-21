public class Stromkostenabrechnung
{
    private double ht;
    private double nt;
    private double tage; 
    private double stromHtPrev;  
    private double stromHtNew;
    private double stromNtPrev; 
    private double stromNtNew;
    private double stromverbrauch;
    private double stromkostenfaktor;
    private double leistungspreisGebuehr; 
    private double verrechnungspreisGebuehr;
    private double mwSt = 0.19 ;
    private double parteiverbrauch, gesamtverbrauch;

    public Stromkostenabrechnung(double ht, double nt, double tage, double stromHtPrev, double  stromHtNew, double stromNtPrev, 
    double stromNtNew, double leistungspreisGebuehr, double verrechnungspreisGebuehr, double parteiverbrauch, double gesamtverbrauch){
        this.ht = ht;
        this.nt = nt;
        this.tage = tage;
        this.stromHtPrev = stromHtPrev;
        this.stromHtNew = stromHtNew;
        this.stromNtPrev = stromNtPrev;
        this.stromNtNew = stromNtNew;
        this.leistungspreisGebuehr = leistungspreisGebuehr;
        this.verrechnungspreisGebuehr = verrechnungspreisGebuehr;
        this.parteiverbrauch = parteiverbrauch;
        this.gesamtverbrauch = gesamtverbrauch;
    }

    public double wohnFaktor(){
        double result = this.tage / 365.0;
        return result;
    }

    public double stromverbrauchHt(){
        double result = this.stromHtNew - this.stromHtPrev;
        return result;
    }

    public double stromverbrauchNt(){
        double result = this.stromNtNew - this.stromNtPrev;
        return result;
    }

    public double heizFaktor(){
        double result = this.parteiverbrauch / this.gesamtverbrauch;
        return result;
    }

    public double arbeitspreisHT(){
        double result = (ht/100) * heizFaktor() * stromverbrauchHt();
        return result;
    }

    public double arbeitspreisNT(){
        double result = (nt/100) * heizFaktor() * stromverbrauchNt();
        return result;
    }

    public double leistungspreis(){
        double result = wohnFaktor() * leistungspreisGebuehr;
        return result;
    }

    public double verrechnungspreis(){
        double result = wohnFaktor() * verrechnungspreisGebuehr;
        return result;
    }

    public double stromkostenGesamt(){
        double no = (arbeitspreisHT() + arbeitspreisNT() + leistungspreis() + verrechnungspreis());
        no = no * (1.0 + this.mwSt);
        System.out.println(no);
        return no;
    }
}










