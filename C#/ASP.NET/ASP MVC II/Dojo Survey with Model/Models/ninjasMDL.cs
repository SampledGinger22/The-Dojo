namespace Dojo_Survey_With_Model.Models {
    public class Ninja {
        public string Name { get; set; }
        public string Location { get; set; }
        public string Language { get; set; }
        public string Comment { get; set; }

        public Ninja(string name, string loc, string lang, string comm){
            Name = name;
            Location = loc;
            Language = lang;
            Comment = comm;
        }
    }
}