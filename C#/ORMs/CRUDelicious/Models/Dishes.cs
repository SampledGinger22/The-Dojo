#pragma warning disable CS8618
using System.ComponentModel.DataAnnotations;

namespace CRUDelicious.Models;

    public class Dish 
    {
        [Key]
        public int DishId { get;set; }
        public string Name { get;set; }
        public string Chef { get;set; }
        public int Tastiness { get;set; }
        public int Calories { get;set; }
        public string? Description { get;set; }
        public DateTime CreatedAt { get;set; } = DateTime.Now;
        public DateTime UpdatedAt { get;set; } = DateTime.Now;

    //     public Dish NewDish(string name, string chef, int tasty, int cal, string description){
    //         Name = name;
    //         Chef = chef;
    //         Tastiness = tasty;
    //         Calories = cal;
    //         Description = description;
    // }
}

    