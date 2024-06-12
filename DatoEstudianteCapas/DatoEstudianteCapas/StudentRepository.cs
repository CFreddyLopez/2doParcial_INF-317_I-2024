using System.Collections.Generic;
using System.Linq;

namespace LayerDataAccess
{
    public class StudentRepository
    {
        private static List<Student> students = new List<Student>
        {
            new Student { _id = 1, _firstName = "Juan", _lastName = "Rojas", _age = 20 },
            new Student { _id = 2, _firstName = "Luis", _lastName = "Flores", _age = 22 },
            new Student { _id = 3, _firstName = "Rodrigo", _lastName = "Castillo", _age = 21 },
            new Student { _id = 4, _firstName = "Pedro", _lastName = "de Leon", _age = 20 }
        };

        public Student GetStudentById(int id)
        {
            return students.FirstOrDefault(s => s._id == id);
        }

        public List<Student> GetAllStudents()
        {
            return students;
        }
    }
}


