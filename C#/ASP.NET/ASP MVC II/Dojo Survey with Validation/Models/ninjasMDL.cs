#pragma warning disable CS8618
using System.ComponentModel.DataAnnotations;

namespace Dojo_Survey_with_Validation.Models {
    public class Ninja {
        [Required]
        public string Name { get; set; }
        [Required]
        public string Location { get; set; }
        [Required]
        public string Language { get; set; }
        [Required]
        public string Comment { get; set; }
    }
}