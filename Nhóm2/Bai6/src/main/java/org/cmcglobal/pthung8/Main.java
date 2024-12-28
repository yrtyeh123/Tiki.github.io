package org.cmcglobal.pthung8;

public class Main {
    public static void main(String[] args) {
        int binhNuoc = 0;

        System.out.println("Hello, World!");
        RobotHutBui robotx1 = new RobotHutBui("XB_1", 10);
        RobotHutBui robotx2 = new RobotHutBui("XB_2", 30);

        System.out.println("Trong luong cua robotx1 la: " + robotx1.getTrongLuong());
        System.out.println("Trong luong cua robotx2 la: " + robotx2.getTrongLuong());

        System.out.println("Luong nuoc trong robotx1 la: " + robotx1.getLuongNuoc());
        robotx1.layNuoc();
        System.out.println("Luong nuoc trong robotx1 sau khi lay nuoc la: " + robotx1.getLuongNuoc());
        binhNuoc += robotx1.chamNuoc();
        System.out.println("Luong nuoc trong robotx1 sau khi cham nuoc la: " + robotx1.getLuongNuoc());
        System.out.println("Luong nuoc trong binh hien tai la: " + binhNuoc);

        robotx2.layNuoc();
        System.out.println("Luong nuoc trong robotx1 sau khi lay nuoc la: " + robotx2.getLuongNuoc());
        binhNuoc += robotx2.chamNuoc();
        System.out.println("Luong nuoc trong robotx1 sau khi cham nuoc la: " + robotx2.getLuongNuoc());
        System.out.println("Luong nuoc trong binh hien tai la: " + binhNuoc);
    }
}
