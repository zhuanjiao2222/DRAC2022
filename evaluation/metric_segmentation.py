import numpy as np


def get_dice(gt, pred, classId=1):
    if np.sum(gt) == 0:
        return np.nan
    else:
        intersection = np.logical_and(gt == classId, pred == classId)
        dice_eff = (2. * intersection.sum()) / (gt.sum() + pred.sum())
        return dice_eff


def get_IoU(gt, pred, classId=1):
    if np.sum(gt) == 0:
        return np.nan
    else:
        intersection = np.logical_and(gt == classId, pred == classId)
        union = np.logical_or(gt == classId, pred == classId)
        iou = np.sum(intersection) / np.sum(union)
        return iou


def get_mean_IoU_dice(gts_list, preds_list):
    assert len(gts_list) == len(preds_list)
    dice_list = []
    iou_list = []
    for gt_array, pred_array in zip(gts_list, preds_list):
        dice = get_dice(gt_array, pred_array, 1)
        iou = get_IoU(gt_array, pred_array, 1)
        dice_list.append(dice)
        iou_list.append(iou)
    mDice = np.nanmean(dice_list)
    mIoU = np.nanmean(iou_list)
    return mDice, mIoU


if __name__ == "__main__":
    # gts_list is a list of ground truth mask images
    # preds_list is a list of predicted mask images
    gt_list = []
    pred_list = []
    mean_Dice, mean_IoU = get_mean_IoU_dice(gt_list, pred_list)