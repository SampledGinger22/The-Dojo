using Microsoft.AspNetCore.Mvc;
using Dojo_Survey_With_Model.Models;
namespace Dojo_Survey_With_Model.Controllers;
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
        public IActionResult formreturn(Ninja ninja){
            return View();
        }
    }