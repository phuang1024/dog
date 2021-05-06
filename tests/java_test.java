/**
 * The ASCIIArt program prints the name "Agastya", the initials AP and a some
 * fish to standard output using ascii characters to make a picture.
 * 
 * @author Agastya Pawate
 * @version long long ago
 * @author Period 4 Intro to CS
 * 
 * @author Assignment:  ASCIIArt
 * 
 * @author Sources: Agastya Pawate
 */
public class ASCIIArt
{
    public ASCIIArt()
    {
        System.out.println( "Agastya's ASCII Art" );
        System.out.println();
    }

    public void firstName()
    {
        // print out Agastya using letters
        System.out.println( "         A                       GG                    A                    SS           TTTTTTTTTTTTTTTTTTTTTT            Y       Y                A  " );
        System.out.println( "        A A                    G    G                 A A                 S     S                  T                        Y     Y                A A   " );
        System.out.println( "       A   A                 G                       A   A              S                          T                         Y   Y                A   A    " );
        System.out.println( "      A     A                G                      A     A             S                          T                          Y Y                A     A   " );
        System.out.println( "     AAAAAAAAA               G                     AAAAAAAAA              SS                       T                           Y                AAAAAAAAA         " );
        System.out.println( "    A         A              G                    A         A                S                     T                           Y               A         A  " );
        System.out.println( "   A           A             G    GGGG           A           A                S                    T                           Y              A           A  "  );
        System.out.println( "  A             A            G      GG          A             A               S                    T                           Y             A             A  " );
        System.out.println( " A               A             G    GG         A               A             S                     T                           Y            A               A  " );
        System.out.println( "A                 A              GG           A                 A        SS                        T                           Y           A                 A " );
    }

    public void initials()
    {
        // System.out.print doesn't attach a trailing newline character. We can
        // do this on our own with \n. The \t's are used for inserting tabs
        System.out.print( "\n\t\tor...\n\n" );

        // print out AP using "tiles"
        System.out.println( "      _/           _/_/      " );
        System.out.println( "    _/  _/       _/    _/    " );
        System.out.println( "   _/_/_/_/      _/_/_/       " );
        System.out.println( " _/       _/     _/        "  );
        System.out.println( "_/         _/    _/        " );

        System.out.print( "\n\t\tor...\n" );
        // print out AP using brackets
        System.out.println( "  _______________________" );
        // Java uses a double back slash (\\) to denote an actual backslash
        // character. The reason for this is because \ is an escape sequence for
        // special ascii characters
        System.out.println( " /                       \\" );
        System.out.println( "|     []          [][]    |" );
        System.out.println( "|   []  []       []   []  |" );
        System.out.println( "|  [][][][]      [][][]   |" );
        System.out.println( "| []      []     []       |" );
        System.out.println( "|[]        []    []       |" );
        System.out.println( " \\_______________________/" );
    }

    public void fish()
    {
        System.out.print( "\n\t\tor...\n" );
        // print out some ascii fish...just because
        System.out.println( "                          ,     " );
        System.out.println( "               ()       _/{     " );
        System.out.println( "        ,_         o  .'   './`>" );
        System.out.println( "        _}\\_ O       / a ((  =< " );
        System.out.println( "   <`\\.'    '. o     '.,__,.'\\_>" );
        System.out.println( "    >    )) e \\           \\)    " );
        System.out.println( "   <_/'.,___,.'                 " );
        System.out.println();
        System.out.println();
        /* System.out.println("         _________________________                      ");
        * System.out.println("        |Miller Middle School     |        ");
        * System.out.println("        |             ____________|                      ");
        * System.out.println("        |            |home of     |                                    ");
        * System.out.println("        |            |the mustangs|   ");
        * System.out.println("        |            |  /`>       |       ");
        * System.out.println("        |            | ||____  ___|                    ");
        * System.out.println("        |               \ \___\ \_|");
        * System.out.println("        |________________`-`___\_\|                                       ");
        * System.out.println("                  | |                ");
        * System.out.println("                  | |                   ");
        * System.out.println("                  | |                    ");
        * System.out.println("                  | |              ");
        * System.out.println("                //  \\              ");
        * System.out.println("//////////////////////////////////////                              ");
        * ^^^^Can't get this to work yet (escape characters error)^^^^ 
        */
    }

    public static void main( String[] args )
    {
        ASCIIArt asciiArtist = new ASCIIArt();
        asciiArtist.firstName();
        asciiArtist.initials();
        asciiArtist.fish();
    } // main
} // ASCIIArt

