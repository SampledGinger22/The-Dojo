using Microsoft.EntityFrameworkCore;
namespace Chefs_n_Dishes.Models;
// the MyContext class representing a session with our MySQL 
// database allowing us to query for or save data
public class MyContext : DbContext 
{ 
    public MyContext(DbContextOptions options) : base(options) { }
    public DbSet<Chef> Chefs { get; set; } = null!;
    public DbSet<Dish> Dishes { get;set; } = null!;

}