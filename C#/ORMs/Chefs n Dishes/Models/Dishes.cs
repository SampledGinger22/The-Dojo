#pragma warning disable CS8618
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Chefs_n_Dishes.Models;

public class Dish
{
    [Key]
    public int DishId { get;set; }
    [Required]
    public string Name { get;set; }
    [Required]
    [Range(1, Int32.MaxValue, ErrorMessage = "Calories must be greater than 0")]
    public int Calories { get;set; }
    [Required]
    public string Description { get;set; }
    [Required]
    [Range(0,6)]
    public int Tastiness { get;set; }
    [Required]
    public int ChefId { get;set; }
    public Chef? Creator { get;set; }
    public DateTime CreatedAt { get;set; } = DateTime.Now;
    public DateTime UpdatedAt { get;set; } = DateTime.Now;
}