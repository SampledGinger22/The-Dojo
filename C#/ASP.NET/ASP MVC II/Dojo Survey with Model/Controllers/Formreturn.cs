using Microsoft.AspNetCore.Mvc;
using Dojo_Survey_With_Model.Models;
namespace Dojo_Survey_With_Model.Controllers;
    public class HomeFormReturn : Controller
    {
        [HttpPost("result")]
        public IActionResult formreturn(Ninja ninja){
            return View("formreturn", ninja);
        }
    }