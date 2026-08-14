import java.io.IOException;

/** Demo runner — runs minMovesToEscape on one example case and prints the result. */
public class Main {
    public static void main(String[] args) throws IOException {
        TestData.TestCase c = TestData.loadCase(TestData.TEST_DATA_DIR + "/simple/04_worked_example_k2.txt");

        System.out.println("Case: " + c.name);
        System.out.println("Grid:");
        for (String row : c.grid) {
            System.out.println("  " + row);
        }
        System.out.println("K = " + c.k);

        int result = EscapeVault.minMovesToEscape(c.grid, c.k);
        System.out.println("Minimum moves to escape: " + result);
    }
}
