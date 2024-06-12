using LayerBusiness;
using System;

namespace Presentation
{
    class Program
    {
        static void Main(string[] args)
        {
            StudentService studentService = new StudentService();

            Console.WriteLine("Enter Student ID:");
            int studentId = int.Parse(Console.ReadLine());

            var student = studentService.GetStudentById(studentId);

            if (student != null)
            {
                Console.WriteLine($"ID: {student._id}");
                Console.WriteLine($"First Name: {student._firstName}");
                Console.WriteLine($"Last Name: {student._lastName}");
                Console.WriteLine($"Age: {student._age}");
            }
            else
            {
                Console.WriteLine("Student not found.");
            }

            Console.ReadKey();
        }
    }
}
