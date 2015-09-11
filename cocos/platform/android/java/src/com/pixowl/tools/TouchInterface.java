package com.pixowl.tools;

public class TouchInterface
{	
	public static native void nativeTouchesBegin(final int id, final float x, final float y);
    public static native void nativeTouchesEnd(final int id, final float x, final float y);
    public static native void nativeTouchesMove(final int[] ids, final float[] xs, final float[] ys);
    public static native void nativeTouchesCancel(final int[] ids, final float[] xs, final float[] ys);
}
