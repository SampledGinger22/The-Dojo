#pragma warning disable CS8618
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
namespace Products_and_Categories.Models;

public class Product
{
    [Key]
    public int ProductId { get;set; }
    [Required]
    public string Name { get;set; }
    [Required]
    public string Description { get;set; }
    [Required]
    [Range(0, 999999999999999999.99)]
    public decimal Price { get;set; }
    public DateTime CreatedAt { get;set; } = DateTime.Now;
    public DateTime UpdatedAt { get;set; } = DateTime.Now;
    List<Association> ProdAssociations = new List<Association>();
}