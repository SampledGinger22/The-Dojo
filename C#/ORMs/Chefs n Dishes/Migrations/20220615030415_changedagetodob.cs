using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Chefs_n_Dishes.Migrations
{
    public partial class changedagetodob : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.RenameColumn(
                name: "Age",
                table: "Chefs",
                newName: "DateOfBirth");
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.RenameColumn(
                name: "DateOfBirth",
                table: "Chefs",
                newName: "Age");
        }
    }
}
