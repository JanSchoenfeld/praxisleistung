
public class WasserTest
{

    public WasserTest()
    {
        Wasserkostenabrechnung wasserkostenabrechnung = new Wasserkostenabrechnung(309, 342, 457, 495, 1.545, 146.16, 365, 1.99);
        double result = wasserkostenabrechnung.wasserKostenBerechnung();
    }
}
