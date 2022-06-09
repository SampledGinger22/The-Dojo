#pragma warning disable CS8618
using System.ComponentModel.DataAnnotations;

namespace Dojo_Survey_with_Validation.Models {
    public class Ninja {
        [Required]
        [MinLength(2, ErrorMessage = "Name must be at least two characters long")]
        public string Name { get; set; }
        [Required]
        public string Location { get; set; }
        [Required]
        public string Language { get; set; }
        [MinLength(20, ErrorMessage = "Must contain at least 20 characters")]
        public string Comment { get; set; } = null!;
    }
}