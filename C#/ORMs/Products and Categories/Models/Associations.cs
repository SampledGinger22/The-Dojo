#pragma warning disable CS8618
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
namespace Products_and_Categories.Models;

public class Association
{
    [Key]
    public int AssociationId { get;set; }
    public int ProductId { get;set; }
    public Product? product { get;set; }
    public int CategoryId { get;set; }
    public Category? category { get;set; }
}