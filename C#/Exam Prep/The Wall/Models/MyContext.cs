using Microsoft.EntityFrameworkCore;
namespace The_Wall.Models;

public class MyContext : DbContext 
{ 
    public MyContext(DbContextOptions options) : base(options) { }
    public DbSet<User> Users { get; set; } = null!;
    public DbSet<Message> Messages { get;set; } = null!;
    public DbSet<Comment> Comments { get;set; } = null!;

}