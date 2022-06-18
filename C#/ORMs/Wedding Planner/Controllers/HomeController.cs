using System.Diagnostics;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Wedding_Planner.Models;
using System.Linq;

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
            return RedirectToAction("LoginandReg", "Login");
        }
        ViewBag.seshid = HttpContext.Session.GetInt32("userid");
        List<Wedding> weddings = _context.Weddings
            .Include(r => r.Users)
                .ThenInclude(r => r.User)
            .ToList();

        return View("Dashboard", weddings);
    }
    

    [HttpGet("weddings/RSVP/{weddingid}")]
    public IActionResult RSVP(int weddingid)
    {
        int? userid = HttpContext.Session.GetInt32("userid");
        int userID = Convert.ToInt32(userid);
        RSVP newRsvp = new RSVP();
        newRsvp.UserId = userID;
        newRsvp.WeddingId = weddingid;

        List<RSVP> rsvpcheck = _context.RSVPs.Where(c => c.WeddingId == weddingid && c.UserId == userid).ToList();

        bool itemcheck = true;
        if(rsvpcheck.Count() == 0){
            itemcheck = false;
        }

        if(itemcheck == false){
            _context.RSVPs.Add(newRsvp);
            _context.SaveChanges();
        }
        else
        {
            if(rsvpcheck.Count() != 0)
            {
                _context.RSVPs.Remove(rsvpcheck[0]);
                _context.SaveChanges();
            }
        }
        return RedirectToAction("Dashboard");
    }

    [HttpGet("weddings/new")]
    public IActionResult NewWedding()
    {
        var userid = HttpContext.Session.GetInt32("userid");
        ViewBag.userid = Convert.ToInt32(userid);
        return View("NewWedding");
    }

    [HttpPost("weddings/new/save")]
    public IActionResult SaveWedding(Wedding wedding)
    {
        if(ModelState.IsValid)
        {
            _context.Weddings.Add(wedding);
            _context.SaveChanges();
            List<Wedding> weddings = _context.Weddings
                .Include(r => r.Users)
                    .ThenInclude(r => r.User)
                .ToList();
            var newWed = weddings.LastOrDefault();
            return View("ViewWedding", newWed);
        }
        else return View("NewWedding");
    }

    [HttpGet("weddings/view/{weddingid}")]
    public IActionResult ViewWedding(int weddingid)
    {
        var wedding = _context.Weddings
            .Include(r => r.Users)
                .ThenInclude(r => r.User)
            .FirstOrDefault(w => w.WeddingId == weddingid);
        return View("ViewWedding", wedding);
    }

    [HttpGet("weddings/delete/{weddingid}")]
    public IActionResult Delete(int weddingid)
    {
        var wedding = _context.Weddings.FirstOrDefault(w => w.WeddingId == weddingid);
        if(wedding != null)
        {
            _context.Weddings.Remove((Wedding)wedding);
            _context.SaveChanges();
            return View("Dashboard");
        }
        return View("Dashboard");
    }

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}
