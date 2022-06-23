#pragma warning disable CS8618
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace The_Wall.Models;

public class Message {

    [Key]
    public int MessageId { get;set; }

    [Required]
    public string Content { get;set; }
    
    public int? UserId { get;set; }

    public User? User { get;set; }

    public DateTime Created_At { get;set; } = DateTime.Now;

    public DateTime Updated_At { get;set; } = DateTime.Now;

    public List<Comment> Comment { get;set; } = new List<Comment>();
}