#pragma warning disable CS8618
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
namespace Products_and_Categories.Models;

public class Category
{
    [Key]
    public int CategoryId { get;set; }
    [Required]
    public string Name { get;set; }
    public DateTime CreatedAt { get;set; } = DateTime.Now;
    public DateTime UpdatedAt { get;set; } = DateTime.Now;
    public List<Association> CategoryProds { get;set; } = new List<Association>();
}