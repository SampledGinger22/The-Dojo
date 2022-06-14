#pragma warning disable CS8618
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Chefs_n_Dishes.Models;

public class Chef
{
    [Key]
    public int ChefId { get;set; }
    [Required]
    public string FirstName { get;set; }
    [Required]
    public string LastName { get;set; }
    [Required]
    [DataType(DataType.Date)]
    [MinimumAge(18, ErrorMessage = "Chef must be at least 18 years of age")]
    public DateTime? Age { get;set; }
    public DateTime CreatedAt { get;set; } = DateTime.Now;
    public DateTime UpdatedAt { get;set; } = DateTime.Now;
    public List<Dish> newDishes { get;set; } = new List<Dish>();
}