using System;

class Program
{
    static void Main()
    {
        Console.Write("Shkruani numrin e studenteve: ");
        int studentCount = int.Parse(Console.ReadLine());
        Console.Write("Shkruani numrin e lëndëve: ");
        int subjectCount = int.Parse(Console.ReadLine());

        int[,] grades = new int[studentCount, subjectCount];
        string[] studentNames = new string[studentCount];
        string[] subjectNames = new string[subjectCount];

        for (int i = 0; i < subjectCount; i++)
        {
            Console.Write($"Shkruani emrin e lëndës {i + 1}: ");
            subjectNames[i] = Console.ReadLine();
        }

        for (int i = 0; i < studentCount; i++)
        {
            Console.Write($"Shkruani emrin e studentit {i + 1}: ");
            studentNames[i] = Console.ReadLine();

            for (int j = 0; j < subjectCount; j++)
            {
                Console.Write($"Shkruani notën për {studentNames[i]} në lëndën {subjectNames[j]}: ");
                grades[i, j] = int.Parse(Console.ReadLine());
            }
        }

        Console.WriteLine("\nRezultatet e Studenteve:");
        Console.WriteLine("----------------------------------------------------");
        Console.Write("Studenti\t");
        foreach (var subject in subjectNames)
        {
            Console.Write(subject + "\t");
        }
        Console.WriteLine("Mesatarja");
        Console.WriteLine("----------------------------------------------------");

        for (int i = 0; i < studentCount; i++)
        {
            Console.Write(studentNames[i] + "\t");
            int total = 0;
            for (int j = 0; j < subjectCount; j++)
            {
                Console.Write(grades[i, j] + "\t");
                total += grades[i, j];
            }
            double average = (double)total / subjectCount;
            Console.WriteLine(average.ToString("0.00"));
        }
    }
}
