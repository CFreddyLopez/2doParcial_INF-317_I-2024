using LayerDataAccess;
using System.Collections.Generic;

namespace LayerBusiness
{
    public class StudentService
    {
        private readonly StudentRepository studentRepository;

        public StudentService()
        {
            studentRepository = new StudentRepository();
        }

        public Student GetStudentById(int id)
        {
            return studentRepository.GetStudentById(id);
        }

        public List<Student> GetAllStudents()
        {
            return studentRepository.GetAllStudents();
        }
    }
}
