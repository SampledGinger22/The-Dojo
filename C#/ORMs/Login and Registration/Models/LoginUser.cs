#pragma warning disable CS8618
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Login_and_Registration.Models;

public class LoginUser
{
    [NotMapped]
    [Required]
    [EmailAddress]
    public string Email { get;set; }
    [NotMapped]
    [Required]
    [MinLength(8, ErrorMessage = "Password must be at least 8 characters in length.")]
    public string Password { get;set; }
}