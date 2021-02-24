using System;
using Microsoft.EntityFrameworkCore.Migrations;

namespace Bachelor2021.DataAccess.Maintenance.Migrations
{
    public partial class FixedImage : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "Data",
                table: "Images");

            migrationBuilder.RenameColumn(
                name: "Suffix",
                table: "Images",
                newName: "Title");

            migrationBuilder.AddColumn<string>(
                name: "ImageName",
                table: "Images",
                type: "nvarchar(max)",
                nullable: true);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "ImageName",
                table: "Images");

            migrationBuilder.RenameColumn(
                name: "Title",
                table: "Images",
                newName: "Suffix");

            migrationBuilder.AddColumn<byte[]>(
                name: "Data",
                table: "Images",
                type: "varbinary(max)",
                nullable: true);
        }
    }
}
