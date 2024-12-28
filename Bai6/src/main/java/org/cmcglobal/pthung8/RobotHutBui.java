package org.cmcglobal.pthung8;

public class RobotHutBui {
    private String model;
    private int theTich;
    private int trongLuong;
    private int luongNuoc;

    public RobotHutBui(String model, int theTich) {
        this.model = model;
        this.theTich = theTich;
        this.trongLuong = theTich * 2 + 100;
        this.luongNuoc = 0;
    }

    public int getTrongLuong() {
        return this.trongLuong;
    }

    public int getLuongNuoc() {
        return this.luongNuoc;
    }

    public void layNuoc() {
        this.luongNuoc = theTich;
    }

    public int chamNuoc() {
        int nuocDoRa = this.luongNuoc;
        this.luongNuoc = 0;
        return nuocDoRa;
    }


}
