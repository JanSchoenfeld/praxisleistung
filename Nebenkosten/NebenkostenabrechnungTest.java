

import static org.junit.Assert.*;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;


public class NebenkostenabrechnungTest
{

    
    public Nebenkostenabrechnung rechnung;
    public NebenkostenabrechnungTest()
    {
    }
    /**
     * Sets up the test fixture.
     *
     * Called before every test case method.
     */
    @Before
    public void setUp()
    {
       this.rechnung = new Nebenkostenabrechnung(22.07, 16.35, 365, 24894, 28084, 12455, 13995,
                                                                    42.95, 61.36, 5625, 11420);
    }

    
    @Test
    public void test1(){
        assertEquals(1.0, rechnung.wohnFaktor(), 0);
    }
    
    @Test
    public void test2(){
        assertEquals(3190.0, rechnung.stromverbrauchHt(), 0);
    }
    
    @Test
    public void test3(){
        assertEquals(1540.0, rechnung.stromverbrauchNt(), 0);
    }
    
    @Test
    public void test4(){
        assertEquals(0.49, rechnung.heizFaktor(), 0.01);
    }
    
    @Test
    public void test5(){
        assertEquals(344.98, rechnung.arbeitspreisHT(), 3);
    }
    
            @Test
    public void test6(){
        assertEquals(123.38, rechnung.arbeitspreisNT(), 3);
    }
    
    @Test
    public void test7(){
        assertEquals(42.95 , rechnung.leistungspreis(), 0);
    }
    
    @Test
    public void test8(){
        assertEquals(61.36 , rechnung.verrechnungspreis(), 0);
    }
    
    
    
        /**
     * Tears down the test fixture.
     *
     * Called after every test case method.
     */
    @After
    public void tearDown()
    {
    }
}
