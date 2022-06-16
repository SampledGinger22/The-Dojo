#pragma warning disable CS8618
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Wedding_Planner.Models;

public class Wedding 
{
    [Key]
    public int WeddingId { get;set; }

    [Required]
    [MinLength(2, ErrorMessage = "Wedder name must be at least two characters in length")]
    public string Wedder_1 { get;set; }

    [Required]
    [MinLength(2, ErrorMessage = "Wedder name must be at least two characters in length")]
    public string Wedder_2 { get;set; }

    [Required]
    public DateTime Date { get;set; }

    [Required]
    public string Address { get;set; }

    public List<RSVP> RSVPs = new List<RSVP>();
}