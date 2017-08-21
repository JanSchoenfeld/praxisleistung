

public class Test
{
     
    public Test()
    {
       Stromkostenabrechnung rechnung = new Stromkostenabrechnung(22.07, 16.35, 365, 24894, 28084, 12455, 13995, 42.95, 61.36, 5625, 5625+5795);
       double result = rechnung.stromkostenGesamt();

    }
}
