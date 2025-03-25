using System;
using System.Collections.Generic;

class Student
{
    public string Name { get; set; }
    public List<int> Grades { get; set; }

    public Student(string name)
    {
        Name = name;
        Grades = new List<int>();
    }

    public void AddGrade(int grade)
    {
        Grades.Add(grade);
    }

    public double GetAverageGrade()
    {
        if (Grades.Count == 0)
            return 0;

        double sum = 0;
        foreach (var grade in Grades)
        {
            sum += grade;
        }
        return sum / Grades.Count;
    }
}

class Program
{
    static void Main()
    {
        List<Student> students = new List<Student>();

        while (true)
        {
            Console.WriteLine("1. Shto student");
            Console.WriteLine("2. Regjistro notë");
            Console.WriteLine("3. Shfaq notat mesatare");
            Console.WriteLine("4. Dil");
            Console.Write("Zgjidhni një opsion: ");
            int choice = int.Parse(Console.ReadLine());

            switch (choice)
            {
                case 1:
                    Console.Write("Shkruani emrin e studentit: ");
                    string name = Console.ReadLine();
                    students.Add(new Student(name));
                    break;
                case 2:
                    Console.Write("Shkruani emrin e studentit: ");
                    name = Console.ReadLine();
                    Student student = students.Find(s => s.Name == name);
                    if (student != null)
                    {
                        Console.Write("Shkruani notën: ");
                        int grade = int.Parse(Console.ReadLine());
                        student.AddGrade(grade);
                    }
                    else
                    {
                        Console.WriteLine("Studenti nuk u gjet!");
                    }
                    break;
                case 3:
                    foreach (var s in students)
                    {
                        Console.WriteLine($"{s.Name} - Nota mesatare: {s.GetAverageGrade():F2}");
                    }
                    break;
                case 4:
                    return;
                default:
                    Console.WriteLine("Opsion i pavlefshëm, provoni përsëri.");
                    break;
            }
        }
    }
}
