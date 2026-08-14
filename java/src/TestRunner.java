import java.io.IOException;
import java.util.List;

/**
 * Test harness for Escape the Vault.
 *
 * Loops over every test case in ../test_data/{simple,medium,hard}/, calls
 * EscapeVault.minMovesToEscape on each, and reports PASS/FAIL per tier.
 * Exits with status 1 if any test fails.
 *
 * Simple and medium cases are small enough to trace by hand; hard cases are
 * larger generated mazes intended to test how your solution scales, not
 * just whether it's correct. See ../test_data/README.md for details on
 * every case.
 */
public class TestRunner {

    private static final String[] TIERS = {"simple", "medium", "hard"};

    public static void main(String[] args) throws IOException {
        int totalPassed = 0;
        int totalFailed = 0;

        for (String tier : TIERS) {
            System.out.println("\n--- " + tier + " ---");
            int[] result = runTier(tier);
            totalPassed += result[0];
            totalFailed += result[1];
            System.out.println(tier + ": " + result[0] + " passed, " + result[1] + " failed");
        }

        System.out.println();
        System.out.println("TOTAL: " + totalPassed + " passed, " + totalFailed + " failed out of "
                + (totalPassed + totalFailed));

        if (totalFailed > 0) {
            System.exit(1);
        }
    }

    private static int[] runTier(String tier) throws IOException {
        List<TestData.TestCase> cases = TestData.loadTier(tier);
        int passed = 0;
        int failed = 0;

        for (TestData.TestCase c : cases) {
            String status;
            String actualStr;
            long start = System.nanoTime();
            try {
                int actual = EscapeVault.minMovesToEscape(c.grid, c.k);
                boolean ok = actual == c.expected;
                status = ok ? "PASS" : "FAIL";
                actualStr = String.valueOf(actual);
                if (ok) {
                    passed++;
                } else {
                    failed++;
                }
            } catch (UnsupportedOperationException e) {
                status = "FAIL";
                actualStr = "NOT IMPLEMENTED";
                failed++;
            }
            double elapsedMs = (System.nanoTime() - start) / 1_000_000.0;
            System.out.printf("[%s] %s/%s: expected=%d actual=%s (%.1fms)%n",
                    status, tier, c.name, c.expected, actualStr, elapsedMs);
        }

        return new int[] {passed, failed};
    }
}
