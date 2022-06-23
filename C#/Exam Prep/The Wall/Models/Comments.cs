#pragma warning disable CS8618
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace The_Wall.Models;

public class Comment {

    [Key]
    public int CommentId { get;set; }

    [Required]
    public string Content { get;set; }

    public DateTime Created_At { get;set; } = DateTime.Now;

    public DateTime Updated_At { get;set; } = DateTime.Now;

    public int? UserId { get;set; }

    public User? User { get;set; }

    public int? MessageId { get;set; }

    public Message? Message { get;set; }
}