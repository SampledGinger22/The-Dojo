#pragma warning disable CS8618
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Login_and_Registration.Models;

public class User 
{
    [Key]
    public int id { get;set; }
    [Required]
    [MinLength(2, ErrorMessage = "First name must be at least two characters in length")]
    public string FirstName { get;set; }
    [Required]
    [MinLength(2, ErrorMessage = "Last name must be at least two characters in length")]
    public string LastName { get;set; }

    [Required]
    [EmailAddress]
    public string Email { get;set; }
    [Required]
    [MinLength(8, ErrorMessage = "Password must be at least 8 characters in length.")]
    public string Password { get;set; }

    [NotMapped]
    [Compare("Password")]
    [DataType(DataType.Password)]
    public string Confirm { get;set; }
}