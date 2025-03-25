using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Mirësevini në Sistemin e Notave!");

        while (true)
        {
            
            Console.Write("Shkruani pikët për detyrat: ");
            int piketDetyrat = int.Parse(Console.ReadLine());

            Console.Write("Shkruani pikët për kuizet: ");
            int piketKuizet = int.Parse(Console.ReadLine());

            Console.Write("Shkruani pikët për provimin: ");
            int piketProvimi = int.Parse(Console.ReadLine());

           
            int notaMesatare = (piketDetyrat + piketKuizet + piketProvimi) / 3;
            char nota;

            if (notaMesatare >= 90)
                nota = 'A';
            else if (notaMesatare >= 80)
                nota = 'B';
            else if (notaMesatare >= 70)
                nota = 'C';
            else if (notaMesatare >= 60)
                nota = 'D';
            else
                nota = 'F';

            Console.WriteLine("\nLlogaritja...");
            Console.WriteLine($"Nota mesatare: {notaMesatare}");
            Console.WriteLine($"Nota: {nota}");

            if (notaMesatare >= 60)
                Console.WriteLine("Urime! Ju keni kaluar kursin.");
            else
                Console.WriteLine("Fatkeqësisht, ju nuk e kaluat kursin.");

            
            Console.Write("\nDëshironi të llogarisni notën për një student tjetër? (po/jo): ");
            string pergjigje = Console.ReadLine().ToLower();

            if (pergjigje != "po")
                break;

            Console.WriteLine();
        }

        Console.WriteLine("Faleminderit që përdorët Sistemin e Notave!");
    }
}
