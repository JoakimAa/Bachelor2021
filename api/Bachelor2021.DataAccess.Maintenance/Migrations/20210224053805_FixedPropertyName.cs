using Microsoft.EntityFrameworkCore.Migrations;

namespace Bachelor2021.DataAccess.Maintenance.Migrations
{
    public partial class FixedPropertyName : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Receipts_Images_MyPropertyimageId",
                table: "Receipts");

            migrationBuilder.RenameColumn(
                name: "MyPropertyimageId",
                table: "Receipts",
                newName: "ImageId");

            migrationBuilder.RenameIndex(
                name: "IX_Receipts_MyPropertyimageId",
                table: "Receipts",
                newName: "IX_Receipts_ImageId");

            migrationBuilder.RenameColumn(
                name: "imageId",
                table: "Images",
                newName: "ImageId");

            migrationBuilder.AddForeignKey(
                name: "FK_Receipts_Images_ImageId",
                table: "Receipts",
                column: "ImageId",
                principalTable: "Images",
                principalColumn: "ImageId",
                onDelete: ReferentialAction.Restrict);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Receipts_Images_ImageId",
                table: "Receipts");

            migrationBuilder.RenameColumn(
                name: "ImageId",
                table: "Receipts",
                newName: "MyPropertyimageId");

            migrationBuilder.RenameIndex(
                name: "IX_Receipts_ImageId",
                table: "Receipts",
                newName: "IX_Receipts_MyPropertyimageId");

            migrationBuilder.RenameColumn(
                name: "ImageId",
                table: "Images",
                newName: "imageId");

            migrationBuilder.AddForeignKey(
                name: "FK_Receipts_Images_MyPropertyimageId",
                table: "Receipts",
                column: "MyPropertyimageId",
                principalTable: "Images",
                principalColumn: "imageId",
                onDelete: ReferentialAction.Restrict);
        }
    }
}
