#pragma warning disable CS8618
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace The_Wall.Models;

class User {

    [Key]
    public int UserId { get;set; }

    [Required]
    [MinLength(2, ErrorMessage = "First name must be at least two characters")]
    public string First_Name { get;set; }

    [Required]
    [MinLength(2, ErrorMessage = "Last name must be at least two characters")]
    public string Last_Name { get;set; }

    [Required]
    [EmailAddress]
    public string Email { get;set; }

    [Required]
    [MinLength(8, ErrorMessage = "Password must be at least 8 characters")]
    public string Password { get;set; }

    [Required]
    [NotMapped]
    [Compare("Password")]
    [DataType(DataType.Password)]
    public string Confirm { get;set; }

    public DateTime Created_At { get;set; } = DateTime.Now;
    public DateTime Updated_At { get;set; } = DateTime.Now;

    public List<Message> Messages { get;set; } = new List<Message>();

    public List<Comment> Comments { get;set; } = new List<Comment>();
}