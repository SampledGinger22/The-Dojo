using Microsoft.EntityFrameworkCore;
namespace Products_and_Categories.Models;
// the MyContext class representing a session with our MySQL 
// database allowing us to query for or save data
public class MyContext : DbContext 
{ 
    public MyContext(DbContextOptions options) : base(options) { }
    public DbSet<Product> Products { get; set; } = null!;
    public DbSet<Association> Associations { get;set; } = null!;
    public DbSet<Category> Categories { get;set; } = null!;

}