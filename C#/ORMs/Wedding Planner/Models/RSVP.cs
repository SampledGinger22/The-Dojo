#pragma warning disable CS8618
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Wedding_Planner.Models;

public class RSVP 
{
    [Key]
    public int RsvpId { get;set; }
    public int UserId { get;set; }
    public User Attendee { get;set; }
    public int WeddingId { get;set; }
    public Wedding Event { get;set; }
}