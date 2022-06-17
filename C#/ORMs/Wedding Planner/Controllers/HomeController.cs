using System.Diagnostics;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Wedding_Planner.Models;

namespace Wedding_Planner.Controllers;

public class HomeController : Controller
{
    private MyContext _context;

    public HomeController(MyContext context)
    {
        _context = context;
    }


    [HttpGet("Dashboard")]
    public IActionResult Dashboard()
    {
        if(HttpContext.Session.GetInt32("userid") == null)
        {
            return RedirectToAction("LoginandReg");
        }
        ViewBag.seshid = HttpContext.Session.GetInt32("userid");
        List<Wedding> weddings = _context.Weddings
            .Include(r => r.Users)
                .ThenInclude(r => r.User)
            .ToList();

        return View("Dashboard", weddings);
    }
    

    [HttpPost("weddings/RSVP/{weddingid}")]
    public IActionResult RSVP(int weddingid)
    {
        var userid = HttpContext.Session.GetInt32("userid");
        RSVP newRsvp = new RSVP();
        newRsvp.UserId = (int)userid;
        newRsvp.WeddingId = weddingid;
        var rsvpcheck = _context.RSVPs.Where(c => c.WeddingId == weddingid).Where(d => d.UserId == userid);
        if(rsvpcheck != null){
            _context.RSVPs.Remove((RSVP)rsvpcheck);
            _context.SaveChanges();
        }
        else
        {
            _context.RSVPs.Add(newRsvp);
            _context.SaveChanges();
        }
        return RedirectToAction("Dashboard");
    }

    public IActionResult Privacy()
    {
        return View();
    }

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}
