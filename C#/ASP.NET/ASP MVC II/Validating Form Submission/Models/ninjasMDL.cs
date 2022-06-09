#pragma warning disable CS8618
using System.ComponentModel.DataAnnotations;

namespace Validating_Form_Submission.Models {
    public class Ninja {
        [Required]
        [MinLength(4, ErrorMessage = "First name must be at least 4 characters")]
        public string FirstName { get; set; }
        [Required]
        [MinLength(4, ErrorMessage = "Last name must be at least 4 characters")]
        public string LastName { get; set; }
        [Required]
        [Range(1, int.MaxValue, ErrorMessage = "Only positive numbers allowed")]
        public int Age { get; set; }
        [Required]
        [EmailAddress(ErrorMessage = "Email Address is Invalid")]
        public string Email { get; set; }
        [Required]
        [MinLength(8, ErrorMessage = "Password must be at least 8 characters")]
        public string Password { get; set; }
    }
}