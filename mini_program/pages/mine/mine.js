//index.js
//获取应用实例
const app = getApp()
/*
* https://developers.weixin.qq.com/miniprogram/dev/reference/configuration/app.html
* */

Page({
  data: {
    image_path: "/static/mine/default_mine.png",
    user_name: "",
    local_address: "请选择"
  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs',
    })
  },
  onLoad: function () {
    if (app.globalData.userInfo) {
      this.setData({
        userInfo: app.globalData.userInfo,
        hasUserInfo: true
      })
    } else if (this.data.canIUse){
      // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
      // 所以此处加入 callback 以防止这种情况
      app.userInfoReadyCallback = res => {
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true
        })
      }
    } else {
      // 在没有 open-type=getUserInfo 版本的兼容处理
      wx.getUserInfo({
        success: res => {
          app.globalData.userInfo = res.userInfo
          this.setData({
            userInfo: res.userInfo,
            hasUserInfo: true
          })
        }
      })
    }
  },
  /*
  * 获取用户绑定信息
  */
    getUserName: function () {
        // 调用微信提供的接口获取用户信息
        wx.getUserInfo({
            success: function (res) {
                console.log("success: ", res)
            },
            fail: function (res) {
                console.log("fail: ", res)
    
            }
        })
    },
  fetch_userinfo: function () {
    wx.openSetting({});
    const that = this;
    wx.getUserInfo({
      success: function (res) {
        console.log(res)
        that.setData({
          user_name: res.userInfo.nickName,
          image_path: res.userInfo.avatarUrl
        })
      },
      fail: function () {
        console.log(res)
      }
    })
  },
  
  /*获取用户位置信息*/
  fetch_address: function () {
    const that = this;
    wx.chooseLocation({
      success: function (res) {
        console.log(res);
        that.setData({
          local_address: res.address
        });
      }
    })
  }
})
