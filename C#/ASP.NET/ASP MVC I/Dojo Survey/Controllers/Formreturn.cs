using Microsoft.AspNetCore.Mvc;
namespace Dojo_Survey.Controllers;
    public class HomeFormReturn : Controller
    {
        [HttpGet("/result")]
        public ViewResult formreturn()
        {
            //Views/Home/HiThere.cshtml
            //Views/Shared/HiThere.cshtml
            return View();
        }

        [HttpPost("result")]
        public IActionResult formreturn(string name, string location, string language, string comment){
            ViewBag.name = name;
            ViewBag.location = location;
            ViewBag.language = language;
            ViewBag.comment = comment;
            return View();
        }
    }