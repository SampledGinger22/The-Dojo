namespace ViewModel_Fun.Models {
    public class User {
        public string FirstName { get; set;}
        public string LastName { get; set; } = null!;

        public User(string fn, string ln){
            FirstName = fn;
            LastName = fn;
        }
        public User(string fn){
            FirstName = fn;
        }
    }
}