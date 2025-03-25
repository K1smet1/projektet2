using System;

class Program
{
    static void Main()
    {
        Console.Write("Shkruani numrin e studentëve: ");
        int n = int.Parse(Console.ReadLine());

        double[] notat = new double[n];

        LexoNotat(notat);

        double mesatarja = LlogaritMesataren(notat);
        double notaMax = GjejMax(notat);
        double notaMin = GjejMin(notat);

        Console.WriteLine($"\nMesatarja e notave: {mesatarja:F2}");
        Console.WriteLine($"Nota më e lartë: {notaMax}");
        Console.WriteLine($"Nota më e ulët: {notaMin}");
    }

    static void LexoNotat(double[] notat)
    {
        for (int i = 0; i < notat.Length; i++)
        {
            Console.Write($"Shkruani notën për studentin {i + 1}: ");
            notat[i] = double.Parse(Console.ReadLine());
        }
    }

   
    static double LlogaritMesataren(double[] notat)
    {
        double shuma = 0;
        foreach (double nota in notat)
        {
            shuma += nota;
        }
        return shuma / notat.Length;
    }

    
    static double GjejMax(double[] notat)
    {
        double max = notat[0];
        foreach (double nota in notat)
        {
            if (nota > max)
                max = nota;
        }
        return max;
    }


    static double GjejMin(double[] notat)
    {
        double min = notat[0];
        foreach (double nota in notat)
        {
            if (nota < min)
                min = nota;
        }
        return min;
    }
}
