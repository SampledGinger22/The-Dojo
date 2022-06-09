using Microsoft.AspNetCore.Mvc;
using Validating_Form_Submission.Models;
namespace Validating_Form_Submission.Controllers;
    
    public class SharedController : Controller
    {
        [HttpPost("result")]
        public ViewResult formreturn(Ninja ninja){
            if(ModelState.IsValid){
                return View("formreturn");
            }
            else {
                return View("form");
            }
        }
    }